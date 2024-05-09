# Kubernetes

Kubernetes를 공부하려면 무엇을 해야할까?
- [devocean의 글](https://devocean.sk.com/blog/techBoardDetail.do?ID=165905&boardType=techBlog)에서 소개하기를 아래의 내용은 단순히 이해가 아니라 내가 다른 사람에게 설명할 수 있을 정도로 공부해야 한다고하니 한번 해보자.

## 컨테이너
- Docker 노트북에 설치
- 리눅스 네임스페이스 & cgropu
- Dockerfile 작성 및 Docker Image 만들기
- Docker Image 실행 / 종료 / 삭제 하기
- Docker Hub에 가입하여 개인 계정에 Image 올리기

## Kubernetes
- Kubernetes 는 누가 만들었을까? 어떻게 해서 나오게 된 것일까? (Google Borg 로 검색)
- CNCF (Cloud Native Computing Foundation) 
    - 이 재단이 어떤 재단인지 알아보기
- Kubernetes 는 기능이 어떤 것들이 있을까?
    - 기본적으로 Kubernetes 는 컨테이너 이미지를 실행시키는 등 관리하는 역할 수행
- Kubernetes 노트북에 설치 (아래 2개 중에 하나)
    - kind
    - minikube
- Kubernetes client 설치
    - kubectl 설치
    - kubectl config 사용법
- Kubernetes Architecture 확인
    - Control plane
        - etcd (key-value store)
        - kube-apiserver
        - kube-controller
        - kube-scheduler
    - Node
        - kube-proxy
        - kubelet
    - Network plugin
- Kubernetes 에서 Pod 란 무엇인가?
- Kubernetes 에 Nginx 이미지를 pod 로 띄우기
    - pod yaml 만들기
    - kubectl 로 pod yaml 을 Kubernetes 에 배포하기
- Pod 는 어떻게 뜨는 것일까?
    - 사용자가 pod yaml 을 작성
    - 사용자가 kubectl 로 pod yaml 을 kubernetes 로 보냄
    - kubernetes api-server 가 이를 받아서 etcd 에 저장
    - kube-scheduler 가 pod 를 원하는 node 로 스케줄링
    - 스케줄링된 node 에 실행중인 kubelet 이 pod 를 실행
- Kubernetes Resource 알아보기
    - Pod
    - ReplicaSet
    - Deployment
    - Label & Selector
    - Service
        - ClusterIP
        - NodePort
        - LoadBalancer
    - Ingress & Ingress Controller
    - StatefulSet
    - DaemonSet
    - StorageClass
    - Persistent Volume
    - Persistent Volume Claim
    - ConfigMap
    - Secret
    - ServiceAccount
    - ClusterRole
    - ClusterRoleBinding
- Custom Controller (Operator 란 무엇인가?)
- CNCF Projects 알아보기
    - Graduated Projects
    - Incubating Projects
    - Sandbox Projects