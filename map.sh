 /usr/local/hadoop-3.1.0/bin/hadoop jar /usr/local/hadoop-3.1.0/share/hadoop/tools/lib/hadoop-streaming-3.1.0.jar \
	-file /home/henry/projects/algorithms/mapper.py    -mapper /home/henry/projects/algorithms/mapper.py \
	-file /home/henry/projects/algorithms/reducer.py   -reducer /home/henry/projects/algorithms/reducer.py \
	-input /home/henry/projects/algorithms/gutenberg/* -output /home/henry/projects/algorithms/gutenberg/gutenberg-output


