from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from app.api.main import api_router
from app.core.config import settings
from fastapi import FastAPI,Request
from app.core.login_secure import verify_token
import time
import uvicorn

from app.models.BaseModels.Bizexception import Bizexception
from app.models.PublicModels.Out import ErrorMod
from app.service.LogService import LogService

# 创建 FastAPI 应用程序实例
app = FastAPI(
    # title=settings.PROJECT_NAME,  # 设置项目名称
    # openapi_url=f"{settings.API_V1_STR}/openapi.json",  # 设置 OpenAPI URL
    # generate_unique_id_function=custom_generate_unique_id,  # 设置生成唯一标识符的函数
    # docs_url=None if settings.ENVIRONMENT == "production" else "/bellybookdoc",  # 禁用 Swagger 文档,
    # redoc_url=None,  # 禁用 Redoc 文档,
)

logger=LogService(name=__name__).getLogger()

HLS_DIR=settings.MSC_HLS_DIR

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有的来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有的方法，包括 OPTIONS
    allow_headers=["Authorization"],  # 允许所有的头部字段
)

@app.exception_handler(Bizexception)
async def custom_exception_handler(request: Request, exc: Bizexception):
    return JSONResponse(
        status_code=200,  # 或者任何其他适当的状态码
        content={"code":f"{exc.error_code}","message": f"{exc.message}"},
    )

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    token=request.headers.get("Authorization")
    url=request.url.path
    logger.info(str(url) + " input_parm=: <headers>" +str(request.headers)+'; <body>' +str(await request.body()))
    if (not verify_token(token)
            and url.find('login-auth')==-1 and url.find('addUser')==-1
            and request.method!='OPTIONS'):
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})
    response = await call_next(request)
    process_time = time.time() - start_time

    # X- 作为前缀代表专有自定义请求头
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(str(url)+" <process_time>: "+str(process_time))
    return response

app.mount("/hls", StaticFiles(directory=HLS_DIR), name="hls")

# 添加主 API 路由器，指定前缀为 API_V1_STR
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
