
# 通过Amazon CDK 在多区域部署 Serverless app 并就近访问

## 项目结构
```bash
Serverless_App_deploy/
├── app_docker/ # 部署的docker镜像
├── bootstrap.sh # 在区域启用bootstrap
├── cdk.json # 配置文件
├── cdk.context.json # 配置文件
├── requirements.txt # 依赖
├── requirements-dev.txt # 依赖
├── README.md # 说明
└── Serverless_App_deploy
    ├── Cloudfrontstack.py # 部署Cloudfront分配及Lambda@edge
    └── route53_stack.py # 部署route53 host zone及创建记录
    └── LambdaApplicationStack.py # 部署Lambda应用并暴露Lambda URL
```

## 环境准备
```bash
# 安装Python3和虚拟环境
sudo apt install python3-venv

# 初始化环境
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 安装CDK CLI（全局）
npm install -g aws-cdk@latest
```

## 部署流程
0. 根据需要修改配置文件 cdk.context.json
定义了需要部署的区域，以及需要部署的域名
1. 在区域启用bootstrap
```bash
./bootstrap.sh
```
1. 部署
```bash
cdk deploy all
```

2. 删除
```bash
cdk destroy all
```