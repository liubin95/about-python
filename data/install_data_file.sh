# file url list
file_list=("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/air_quality_no2.csv")
# down load file from url
for file_url in "${file_list[@]}"
do
    echo "down load file from url: ${file_url}"
    curl -O "${file_url}"
done