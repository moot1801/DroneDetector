import pywt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

paths = []
paths.append(Path(r"C:\AIEEE\DATASET\Processed_CardRF\Train\UAV"))
paths.append(Path(r"C:\AIEEE\DATASET\Processed_CardRF\Train\UAV_Controller"))
output_paths = []
output_paths.append(Path(r"C:\AIEEE\DATASET\Haar\Train\UAV"))
output_paths.append(Path(r"C:\AIEEE\DATASET\Haar\Train\UAV_Controller"))
for k,p in enumerate(paths):
    approx_dir = Path(output_paths[k] / "approx")
    details_dir = Path(output_paths[k] / "details")

    csv_files = list(p.rglob("*.csv"))  # 모든 하위 폴더 포함
    print(f"총 {len(csv_files)}개의 CSV 파일이 있습니다.")
    # 읽기 예시
    all_data = []
    for f in csv_files:
        # 임시 파일이나 깨진 파일 무시
        if f.name.startswith('~$'):
            continue
        try:
            df = pd.read_csv(f)
            df.name= f.name.replace(".csv", "")
            all_data.append(df)
        except Exception as e:
            print(f"⚠️ 오류: {f.name} → {e}")

    print(f"총 {len(all_data)}개의 CSV 파일이 있습니다.")

    for i, df in enumerate(all_data):
        print(f"Processing file {i+1}/{len(all_data)}: {df.name}")
        # 데이터가 비어있거나 컬럼이 없으면 무시
        if df.empty or df.shape[1] == 0:
            print(f"⚠️ 파일 {i+1}은 비어있거나 컬럼이 없습니다.")
            continue
        
        
        # Haar 웨이블릿 변환
        approx, details = pywt.dwt(df.iloc[:, :1024], 'haar')
        filename1 = f"{df.name}_approx.csv"
        filename2 = f"{df.name}_details.csv"
        f1 = pd.DataFrame(approx)
        f1["label"]=f'{df.name}'
        f2 = pd.DataFrame(details)
        f2["label"]=f'{df.name}'

        # 변환된 계수 출력
        f1.to_csv(approx_dir / filename1, index=False, header=False)
        f2.to_csv(details_dir / filename2, index=False, header=False)

