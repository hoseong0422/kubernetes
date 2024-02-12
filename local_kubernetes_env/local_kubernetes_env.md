# Local kubernetes ENV
- local kubernetes 환경 구성을 위해 minikube 이용하여 로컬 쿠버네티스 환경 구성
    - PC : m2 macbook pro
    - driver : docker
    - container runtime : docker
    ```
    minikube start driver=docker
    ```
- Helm 이용한 fluent-bit 설치
    - Helm repo 추가
        ```
        helm repo add fluent https://fluent.github.io/helm-charts
        ```
    - default 설치
        ```
        helm install fluent-bit fluent/fluent-bit
        ```
    - [helm chart version 0.43.0, appVersion 2.2.2 dafault values.yaml](fluent-bit/values.yaml)
    - values 파일 이용 커스텀 설치
        ```
        helm install fluent-bit fluent/fluent-bit -f custom-values.yaml -n log-shipper
        ``` 
        - values 파일 경로 지정 및 namespace 지정 가능
    - values 파일 수정후 배포된 fluent-bit upgrade
        ```
        helm upgrade fluent-bit fluent/fluent-bit -f custom-values.yaml -log-shipper
        ```
    - helm으로 배포된 어플리케이션 삭제
        ```
        helm uninstall fluent-bit -n log-shipper
        ```
        - namespace 지정 없이 삭제시 에러 발생
            ```
            Error: uninstall: Release not loaded: fluent-bit: release: not found
            ```