# A class to contain all the  data list.

class DataListContainer:
    def __init__(self, asciiList, win1252EncodeList):
        self.asciiList = asciiList
        self.win1252EncodeList = win1252EncodeList


# ascii <=> win1252 对照列表
# （少一个符号： \ = %5C）
asciiList = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
             '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
             ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

#16进制的win1252字符集
win1252EncodeList = ['%20', '%21', '%22', '%23', '%24', '%25', '%26', '%27', '%28', '%29', '%2A', '%2B', '%2C',
                     '%2D', '%2E', '%2F', '%30', '%31', '%32', '%33', '%34', '%35', '%36', '%37', '%38', '%39',
                     '%3A', '%3B', '%3C', '%3D', '%3E', '%3F', '%40', '%41', '%42', '%43', '%44', '%45', '%46',
                     '%47', '%48', '%49', '%4A', '%4B', '%4C', '%4D', '%4E', '%4F', '%50', '%51', '%52', '%53',
                     '%54', '%55', '%56', '%57', '%58', '%59', '%5A', '%5B', '%5D', '%5E', '%5F', '%60', '%61',
                     '%62', '%63', '%64', '%65', '%66', '%67', '%68', '%69', '%6A', '%6B', '%6C', '%6D', '%6E',
                     '%6F', '%70', '%71', '%72', '%73', '%74', '%75', '%76', '%77', '%78', '%79', '%7A', '%7B',
                     '%7C', '%7D', '%7E']
