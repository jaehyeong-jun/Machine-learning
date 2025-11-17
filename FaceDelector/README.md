📌 얼굴(Face) vs 동물(Animal) 이미지 분류기

Convolutional Neural Network(CNN) 기반 이진 이미지 분류 모델 개발

📁 프로젝트 개요

사람 얼굴 이미지와 동물 이미지를 구분하는 CNN 모델을 직접 구현 및 학습시키는 프로젝트입니다.
OpenCV로 이미지 전처리 → Keras/TensorFlow로 CNN 모델 구성 → 모델 학습 및 테스트 흐름으로 진행하였습니다.

이 프로젝트는 이미지 데이터 로딩 → 전처리 → 모델 구성 → 학습 → 평가 → 예측 전체 파이프라인을 직접 구현한 점에서 의미가 큽니다.

🎯 목표

얼굴과 동물 이미지를 높은 정확도로 분류하는 CNN 모델 제작

이미지 전처리(BGR→RGB, Resize), 정규화 이해

입력/학습용 데이터 array 형태 구성 경험

CNN 구조 설계 및 overfitting 방지 실습

모델 저장 및 로드 후 예측

🛠 사용 기술
분야	사용 기술
언어	Python
딥러닝	TensorFlow(Keras), CNN(Conv → Pool → Dense)
이미지 처리	OpenCV(cv2)
데이터 처리	NumPy
시각화	Matplotlib


이미지 전처리
image = cv2.imread(file)
image = cv2.resize(image, (64, 64))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

정규화: X_train = X_train / 255.0

CNN 모델 구조
model.add(Conv2D(128, (3, 3), activation="relu"))
model.add(MaxPooling2D())
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPooling2D())
model.add(Conv2D(32, (3, 3), activation="relu"))
model.add(MaxPooling2D())
model.add(Conv2D(32, (3, 3), activation="relu"))
model.add(MaxPooling2D())

model.add(Flatten())
model.add(Dense(64, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(2, activation="softmax"))


특징

Conv 층에서 점점 필터 수 감소 → 파라미터 수 최적화

4단계 Convolution + Pooling

Dense Layer 두껍게 구성 → 학습 능력 강화

출력층 softmax: [사람, 동물]

학습 결과
history = model.fit(X_train, y, epochs=200)
model.save("FACE_DETECTOR.keras")

model.evaluate(X_train, y)


훈련 셋이 30장으로 매우 적음에도 불구하고
소규모 데이터 기준에서는 높은 정확도 확보됨.

(데이터가 적기 때문에 일반화 성능은 과제로 남음 → 개선 가능!)
