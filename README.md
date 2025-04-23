
# Welcome to your CDK Python project!
# 通过Amazon CDK 在多区域部署 SearxNG并就近访问

## 项目结构
```bash
searxng_deploy/
├── app_docker/ # 部署的docker镜像
├── bootstrap.sh # 在区域启用bootstrap
├── cdk.json # 配置文件
├── cdk.context.json # 配置文件
├── requirements.txt # 依赖
├── requirements-dev.txt # 依赖
├── README.md # 说明
└── searxng_deploy
    ├── searxng_deploy_stack.py # 部署lambda函数和cloudfront+lambda edge
    └── route53_stack.py # 部署route53
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