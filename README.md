# K8s Pod Autocreate
---

## 코드 실행
```bash
$ ./mwcreate -h
usage: mwcreate [-h] -c COMMAND [-n JOB_NAME] [-g GPU_COUNT] [-i IMAGE_NAME]

MW OST Tool

optional arguments:
  -h, --help            show this help message and exit
  -c COMMAND, --command COMMAND
                        Run command
  -n JOB_NAME, --name JOB_NAME
                        Select job name
  -g GPU_COUNT, --gpus GPU_COUNT
                        Number of GPU usage. Default=0
  -i IMAGE_NAME, --image IMAGE_NAME
                        Select image
```

::Options::
* -c , --command
	* 필수 옵션
	* Pod 생성 시 실행할 Command 입력
* -n , --name
	* 생성할 Pod 이름 설정
	* Default : <USER NAME>-autocreate-<IDX> 로 겹치지 않게 자동 생성
* -g , --gpus
	* 사용할 GPU 개수 설정
	* CPU 만 사용 시 0 으로 설정
	* Default : 0
* -i , --image
	* Pod  생성 시 사용할 이미지 입력
	* Default: nvidia/cuda:11.4.1-base-ubuntu20.04


## 코드 실행 예시
```bash
$ ./mwcreate -c "free" -n test1 -g 0 -i ubuntu:20.04
>>>
****************************************
-Miruware-
Made by Suseong Yang
Email : tntjd5596@miruware.com, mw@miruware.com
****************************************

command : free
job_name : test1
gpus : 0
image : ubuntu:20.04
user : yss
uid : 1001
------------------------
pod/test1 created
```

::Pod 생성 확인::
```bash
$ kubectl get pod
>>>
NAME               READY   STATUS      RESTARTS   AGE
test1              0/1     Completed   0          52s
```
