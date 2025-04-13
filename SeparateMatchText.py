filtered_filenames_path = "./KIT-ML/kitML-filtered-filenames.txt"
val_filenames_path = "./KIT-ML/val.txt"
output_matched_filenames_val_path = "./KIT-ML/KIT-ML/val.txt"

# filtered_filenames_path = "./KIT-ML/kitML-filtered-filenames.txt"
# val_filenames_path = "./KIT-ML/train_val.txt"
# output_matched_filenames_val_path = "./KIT-ML/KIT-ML/train_val.txt"

# filtered_filenames_path = "./KIT-ML/kitML-filtered-filenames.txt"
# val_filenames_path = "./KIT-ML/train.txt"
# output_matched_filenames_val_path = "./KIT-ML/KIT-ML/train.txt"

# filtered_filenames_path = "./KIT-ML/kitML-filtered-filenames.txt"
# val_filenames_path = "./KIT-ML/test.txt"
# output_matched_filenames_val_path = "./KIT-ML/KIT-ML/test.txt"

# Read filtered filenames
with open(filtered_filenames_path, "r") as file:
    filtered_filenames = {line.strip() for line in file.readlines()}

# Read val.txt filenames
with open(val_filenames_path, "r") as file:
    val_filenames = {line.strip() for line in file.readlines()}

# Find intersection
matched_filenames_val = val_filenames.intersection(filtered_filenames)

# Save matched filenames
with open(output_matched_filenames_val_path, "w") as file:
    file.write("\n".join(sorted(matched_filenames_val)))

# Preview matched filenames
matched_filenames_val_list = sorted(matched_filenames_val)
print(matched_filenames_val_list[:10])
