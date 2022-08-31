# Load necessary packages
pacman::p_load(xesreadR, tidyverse)

# Import the data - may take many seconds, probably less than a minute
data <- read_xes(xesfile = "bpi_challenge_2013_incidents.xes")

# Turn into regular dataframe
data <- data.frame(data)

# narrow down to just data we are interested in 
data <- subset(data, select = (names(data) %in% c("CASE_concept_name","activity_id")))

# # Check unique symbols - to figure out what to recode as
# unique(data$activity_id)

# Replace as follows:
# "Accepted"  = a
# "Queued"    = b
# "Completed" = c
# "Unmatched" = d

# Recode data
data$activity_id[data$activity_id == "Accepted"] <- "a"
data$activity_id[data$activity_id == "Queued"] <- "b"
data$activity_id[data$activity_id == "Completed"] <- "c"
data$activity_id[data$activity_id == "Unmatched"] <- "d"

# turn into list by splitting based on case
list_data <- split(data$activity_id, f = data$CASE_concept_name)

# Collapse into single strings
# paste(list_data$`1-364285768`, collapse = "")
for(i in 1:length(list_data)){
  list_data[[i]] <- paste(list_data[[i]], collapse = "")
}

# Convert to array
array_data <- array(unlist(list_data))

# Convert to data frame
array_data <- data.frame(array_data)

# load required package and then save data in nice format
write_delim(array_data, "transformed_data", delim = ",", col_names = FALSE)
