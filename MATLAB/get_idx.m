function idx = get_idx(file_path)
    data = load(file_path);
    raw = data.Channel_1.Data;
    signal = double(raw);
    len = length(signal);
    signal_crop = signal(len/100:len/100*99);
    idx = findchangepts(signal_crop, 'MaxNumChanges', 1, 'Statistic', 'mean') + len/100 -1;
end
