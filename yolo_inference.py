# from ultralytics import YOLO

# model = YOLO('yolov8x')

# results =  model.predict('input_videos/08fd33_4.mp4', save = True)
# print(results[0])
# print("=================================================")
# for box in results[0].boxes:
#     print(box)



from ultralytics import YOLO
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")


model = YOLO('models/best.pt').to(device)


results = model.predict('input_videos/08fd33_4.mp4', save=True)

print(results[0])
print("=================================================")
for box in results[0].boxes:   # type: ignore
    print(box)
