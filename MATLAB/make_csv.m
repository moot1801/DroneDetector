folder = "C:\AIEEE\DATASET\CARDRF\LOS\Train\UAV_Controller\DJI_M600";

savepath = "C:\AIEEE\DATASET\changePoints\LOS\Train\UAV_Controller";

files = dir(fullfile(folder, '*.mat'));
results = {};

for i = 1:length(files)
    try
        file_path = fullfile(folder, files(i).name);
        idx = get_idx(file_path);
        results{end+1, 1} = idx;
        results{end, 2} = files(i).name;
    catch e
        warning("Error in %s: %s", files(i).name, e.message);
    end
end

T = cell2table(results, 'VariableNames', {'ChangePoint', 'FileName'});
writetable(T, fullfile(savepath, 'DJI_M600.csv'));