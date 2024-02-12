# test_app
- docker 이미지 빌드
    ```
    # Dockerfile과 동일한 경로에서
    docker build -t python-dummy-logger:0.0.1 .
    ```
    - 이미지 빌드전 `eval $(minikube docker-env)` 이용하여 minikube와 docker host를 연결하여 이미지를 가져올수있도록 해준다.
- 이미지 동작 테스트
    ```
    docker run python-dummy-logger:0.0.1
    ```
- docker 이미지를 이용해 kubernetes 배포
    ```
    kubectl create deployment python-dummy-logger --image=python-dummy-logger -n logging
    ```
    - k9s 이용하여 dummy-logger의 출력 확인
    ![dummy_logger](images/dummy_logger_stdout.png)