import glob

import cv2
from argparse import ArgumentParser
from ultralytics import YOLO


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--model", type=str, default="yolov8n_rgb", help="name of the model")
    parser.add_argument("--folder_path", type=str, default="data_rgb", help="path to a dataset")
    parser.add_argument("--export", type=str, default="", help="export path")

    args = parser.parse_args()
    model = YOLO(f'http://localhost:8000/{args.model}', task='detect')

    if args.export:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(args.export, fourcc, 15, (640, 640))

    for filename in glob.glob(f'{args.folder_path}/*.jpg'):

        frame = cv2.imread(filename)
        frame = cv2.resize(frame, [640, 640], interpolation=cv2.INTER_AREA)

        results = model.predict(frame)

        if len(results) > 0:
            for r in results:
                res_plotted = r.plot()  # allows you to retrieve the prediction results
                cv2.imshow("Frame", res_plotted)
                if args.export:
                    video_writer.write(res_plotted)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    if args.export:
        video_writer.release()
