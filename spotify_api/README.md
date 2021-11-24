# Steps To Creating a New CSV
1) separate_csv .py
   1) I think this adds a empty column.
   2) Did this because if we fail processing one block our entire work is not thrown away. 
   It's a failsafe. It also allows us to share these chunks with one another to 
   finish the process faster. Could also possibly parallelize each block, but I wasn't able to.
      1) I Think it would be difficult because I was having problems with the second part 
      of this process (read add_date.py code)
2) add_date .py
   1) This one is a bit finicky. Read the code to see why it took like 9 hours
3) clean_emptycsv .py
   1) Ended up doing manually because of a an empty column I couldn't remove
4) merge .py
   1) Combine all the files. I had to manually remove an empty column once again.

Finally get an updated spotify data that has the date category: **SpotifyWithDate.csv**