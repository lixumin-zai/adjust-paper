# python3.7
# -*- coding: utf-8 -*-
# @Author : listen
# @Time   :

import time
from io import BytesIO
import cv2
import numpy as np
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos import CosClientError

import sys
import logging
import uuid


logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 设置用户属性, 包括secret_id, secret_key, region
# appid已在配置中移除,请在参数Bucket中带上appid。Bucket由bucketname-appid组成
secret_id = "AKIDTlnY2GCrFNEo79uObXCaopb8PQJxLUN1"  # 替换为用户的secret_id
secret_key = "QaU8WeW9WeXAYhaEdmeGdkaBVbQzINCl"  # 替换为用户的secret_key
region = 'ap-guangzhou'  # 替换为用户的region
token = None  # 使用临时密钥需要传入Token，默认为空,可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token)  # 获取配置对象
client = CosS3Client(config)
uid = uuid.uuid1()
# # 文件流 简单上传
file_name = "image/processed/img/" + str(uid) + '.png'

# 高级上传接口(推荐)


def main():
    response = client.upload_file(
        Bucket='dzl-1305429330',
        LocalFilePath='./process_img/result/process_img.png',
        Key=file_name,
        PartSize=10,
        MAXThread=10
    )
    return uid, response

if __name__ == "__main__":
    main()

# print(response)

# 文件下载 捕获异常
# print(time.time())
# try:
#     response = client.get_object(
#         Bucket='dzl-1305429330',
#         Key='image/processed/img/{}.png'.format(uid),
#     )
#     fp = response['Body'].get_raw_stream()
#     # print(fp.read())
#     # print(time.time())
#     image = cv2.imdecode(np.asarray(bytearray(fp.read()),dtype='uint8'), cv2.IMREAD_COLOR)
#     cv2.imwrite("1234.png", image)
#     # print(time.time())
#
#
# except CosServiceError as e:
#     print(e)
#     # print(e.get_origin_msg())
#     # print(e.get_digest_msg())
#     # print(e.get_status_code())
#     # print(e.get_error_code())
#     # print(e.get_error_msg())
#     # print(e.get_resource_location())
#     # print(e.get_trace_id())
#     print(e.get_request_id())
