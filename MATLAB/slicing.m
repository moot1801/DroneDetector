% [1] 데이터 불러오기 (.mat 파일에 따라 수정)
mat = load("C:\AIEEE\DATASET\CARDRF\LOS\Train\UAV\BEEBEERUN\FLYING\BEEBEERUN_0000100013.mat");
raw = mat.Channel_1.Data;
signal = double(raw);
% [2] 전압 변환 (선택) — 실제 전압 단위로 변환
% yinc = mat.Channel_1.YInc;
% yorg = mat.Channel_1.YOrg;  % 또는 YDispOrigin
% signal = raw * yinc + yorg;

% 정규화: 평균 0, 표준편차 1
signal = signal - mean(signal);
signal = signal / std(signal);

% [5] 변화점 탐지 (mean 기준, 최대 1개 탐색)
signal_crop = signal(1000:4950000);  % 앞쪽 DC/잡음 무시
idx = findchangepts(signal_crop, 'Statistic', 'mean', 'MaxNumChanges', 1);
transient_start = idx + 1000 - 1;  % 원래 인덱스로 복원

% [6] Transient 구간 추출 (길이 1024)
segment_len = 1024;
transient = signal(transient_start : transient_start + segment_len - 1);

% [7] Steady 구간 추출 (transient 뒤 충분히 떨어진 구간)
gap = 5000;
steady_start = transient_start + segment_len + gap;
steady = signal(steady_start : steady_start + segment_len - 1);

% [8] 결과 출력
fprintf('Transient 시작 인덱스: %d\n', transient_start);
fprintf('Steady 시작 인덱스: %d\n', steady_start);
plot(signal);
