#!/bin/bash

# 设置颜色输出
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 检查 cdk.context.json 文件是否存在
if [ ! -f "cdk.context.json" ]; then
    echo -e "${RED}Error: cdk.context.json file not found${NC}"
    exit 1
fi

# 获取账户ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to get AWS account ID${NC}"
    exit 1
fi

echo "Using AWS Account ID: $ACCOUNT_ID"

# 检查 jq 是否安装
if ! command -v jq &> /dev/null; then
    echo -e "${RED}Error: jq is not installed. Please install it first.${NC}"
    exit 1
fi

# 从 cdk.context.json 读取区域
REGIONS=$(jq -r '.searxng_regions[]' cdk.context.json 2>/dev/null)
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to read searxng_regions from cdk.context.json${NC}"
    exit 1
fi

EDGELAMBDA_REGION=$(jq -r '.edgelambda_region' cdk.context.json 2>/dev/null)
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to read edgelambda_region from cdk.context.json${NC}"
    exit 1
fi

# 检查是否成功获取到区域
if [ -z "$REGIONS" ] || [ -z "$EDGELAMBDA_REGION" ]; then
    echo -e "${RED}Error: No regions found in cdk.context.json${NC}"
    exit 1
fi

# 合并区域列表
REGIONS="$REGIONS $EDGELAMBDA_REGION"

# 去重
REGIONS=$(echo "$REGIONS" | tr ' ' '\n' | sort -u | tr '\n' ' ')

echo "Regions to bootstrap: $REGIONS"

# 对每个区域执行 bootstrap
for region in $REGIONS; do
    echo -e "\n${GREEN}Processing region: $region${NC}"
    
    if cdk bootstrap "aws://$ACCOUNT_ID/$region"; then
        echo -e "${GREEN}Successfully bootstrapped $region${NC}"
    else
        echo -e "${RED}Failed to bootstrap $region${NC}"
        exit 1
    fi
done

echo -e "\n${GREEN}Bootstrap process completed${NC}"