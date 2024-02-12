# GKE PoC
- [테스트 로거 이미지 생성 ( Python )](test_app/)
    - 5초 주기로 샘플 로그 출력하는 테스트 로거
    ``` 출력 예시
    {"timestamp": "2024-02-11T00:08:53.004094Z", "level": "INFO", "message": "Test Logger Message", "topic": "test_topic_A"}
    {"timestamp": "2024-02-11T00:08:58.009911Z", "level": "INFO", "message": "Test Logger Message", "topic": "test_topic_B"}        
    {"timestamp": "2024-02-11T00:09:03.012564Z", "level": "INFO", "message": "Test Logger Message", "topic": "test_topic_C"}```
- [쿠버네티스 로컬 환경 구성 ( Minikube )](local_kubernetes_env/)
    - Fluent-Bit 설치 ( Helm )
    - 쿠버네티스 로컬 환경 로그 파싱 테스트
- GKE 환경 Fluent-Bit 설치 ( Helm & Argo CD )
- GKE 환경 로그 파싱 테스트