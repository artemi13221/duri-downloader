import requests
import os

print("**주의사항**")
print("시작하기 전에 폴더 안에 파일들을 모두 비워주시기 바랍니다.")
print("항상 저작권법에 주의하시기 바랍니다. 제작자는 저작권법에 대한 피해에 책임지지 않습니다.")

# m3u8 Download
DOWNLOAD_URL = input("INPUT m3u8 LINK : ")
download_file = requests.get(DOWNLOAD_URL, allow_redirects=True)

m3u8_file = open('download_file.m3u8', 'wb',).write(download_file.content)

tmp = (str(download_file.content)).replace('\'', '')
file_list = tmp.split('\\n')

ts_file_name = file_list[-3]
tmp = ts_file_name.split('_')
ts_file_name = tmp[0] + '_' + tmp[1]
ts_file_index = int((tmp[2].split('.'))[0])

# print(ts_file_index)
# print(ts_file_name)
DOWNLOAD_URL = DOWNLOAD_URL.split('chunklist')[0]


# .ts Download
download_ts_file = []
for i in range(ts_file_index + 1) :
  ts_file = requests.get(DOWNLOAD_URL + ts_file_name + '_' + str(i) + '.ts', allow_redirects=True)
  f = open(ts_file_name + '_' + str(i) + '.ts', 'wb')
  f.write(ts_file.content)
  f.close()
  download_ts_file.append(f.name)


# Combine -> mp4
command_ffmpeg = "ffmpeg -i download_file.m3u8 output.mp4"
os.system(command_ffmpeg)

# 삭제
for i in range(len(download_ts_file)):
  os.remove(download_ts_file[i])
os.remove('download_file.m3u8')

print('done!!')