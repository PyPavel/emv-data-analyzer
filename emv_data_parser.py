import emv_tags_db

def parse_emv_data_block(emv_data_block):
    pairs = list([emv_data_block[i:i + 2] for i in range(0, len(emv_data_block), 2)])
    tags = []
    i = 0
    while i < len(pairs):
        try:
            tag = ""
            temp = []
            if pairs[i] == "9F" or pairs[i] == "5F":
                temp.append(pairs[i]+pairs[i+1])
                tag = pairs[i]+pairs[i+1]
                i+=1
            else:
                temp.append(pairs[i])
                tag = pairs[i]
            temp.append(pairs[i+1])
            b = ""
            for j in range(i+2,int(pairs[i+1],16)+i+2):
                b+=pairs[j]
            temp.append(b)
            tags.append(temp)
            i=int(pairs[i+1],16)+i+2
        except IndexError:
            if(len(tag)):
                print("Tag "+tag+" mallformed!!")
            else:
                print("Parsing error data block corrupted")
            break;
        except Exception:
            print("EMV data block is not correct , correct form is Tag+Len+Value")
            break;
    return tags

def tag_len_value_to_string(tag_len_value):
    outstr = ""
    for i in tag_len_value:
        tag_name_str = ""
        for tag in emv_tags_db.tags:
            if i[0] in tag:
                tag_name_str += "\n" + tag[0];
        outstr += "Tag: " + i[0] + tag_name_str +"\nData Length: " + i[1] + "\nValue: " + i[2] +"\n\n"
    return outstr

