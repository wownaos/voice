import psutil
import numpy as np
import os
import librosa
import pickle
from pathlib import Path
with open("over_20_df.pickle", 'rb') as f:
    over_20_df = pickle.load(f)

"""
labeltext의 빈도수가 20개 이상인 wav파일의 각각의 절대경로를 가져와 librosa를 이용해 array데이터 load

wavlist 함수에서 wav 파일의 각각의 절대경로를 가져와 librosa를 통해 array데이터를 concat하기위한 함수

worker multiprocessing을 동작하기 위한 함수

_check_usage_of_cpu_and_memory 메모리 사용량을 알기위한 함수

labeltext의 경로를 이용해 wav파일을 가져와서 2차원 배열에 효과적으로 불러오는 것

"""


def _check_usage_of_cpu_and_memory():

    """
    메모리 사용량을 체크하기 위한 함수
    parameters 없다
    return 없다
    """    

    memory_usage = psutil.virtual_memory().percent
    available_memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    cpu_usage = psutil.cpu_percent()

    print(f"cpu usage: {cpu_usage}")
    print(f"memory usage: {memory_usage}")
    print(f"available_memory: {available_memory}")


# def wavlist(rootdir,d,wav_lis):
    
#     """
#     모든 wav 파일을 librosa를 통해 array데이터를 가진 list로 반환하는 함수
#     parameters : audio_path, labeltext wav file 명, 데이터를 담을 빈 리스트
#     return : wav_list에 각 wav파일의 경로를 통해 array데이터를 가진 list값 반환
#     """

#     # pathlib 모듈은 모든 하위 디렉토리를 나열함
#     for path in Path(rootdir).iterdir():

#         # path가 디렉토리일시 재귀함수로 하위 디렉토리 입장
#         # path.is_dir(), path.is_file() - return bool
#         if path.is_dir():
#             wavlist(path,d,wav_lis)
        
#         # path가 파일이면 wav리스트에 저장
#         elif path.is_file():
#             if str(path)[62:] == d:
#                 arr, _ = librosa.load(str(path),sr=48000)
#                 wav_lis.append(arr)
#                 #wav_lis.append(str(path))

#     _check_usage_of_cpu_and_memory()
#     return wav_lis

def wavlist(d):
    try:
        if d[63:] in list(over_20_df['FileName']):
            arr, _ = librosa.load(d, sr=48000)
            print('성공')
            #wav_list.append(arr)
    except:
        print('에러발생')
    return arr





def Worker(d):

    """
    병렬로 실행하기 위한 함수
    parameters : labeltext의 빈도수가 20개 이상인 오디오 파일명
    return : wavlist 함수를 거쳐 나온 labeltext의 빈도수가 20개 이상인 오디오파일의 절대경로를 모아둔 리스트
    """

    # 사용되는 process id, worker가 사용하느 자원을 측정해야함(1개의 process가 할당되는 메모리양)
    # 모든 wav 파일 list
    # wav_list = []
    wav = wavlist(d)

    return wav