pacman::p_load(tidyverse, xesreadR)
data <- read_xes(xesfile = "bpi_challenge_2013_incidents.xes")
# turn into regular dataframe
data <- data.frame(data)
# narrow down to just data we are interested in
data <- subset(data, select = (names(data) %in% c("CASE_concept_name","activity_id")))

# Check unique symbols
unique(data$activity_id)
# Replace as follows:
# "Accepted"  = a
# "Queued"    = b
# "Completed" = c
# "Unmatched" = d
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

# Save in nice format
write.csv(array_data, file = "tranformed_data.csv")
