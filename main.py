from PIL import Image, ImageFont, ImageDraw
import textwrap
import csv
import os


def create_custom_postcard():

    IMAGE = Image.open('/Users/user/Dev/custom_postcard/back.png')

    # fonts
    SMALL_FONT = ImageFont.truetype('/Users/user/Dev/custom_postcard/myFont.otf', 55)
    BIG_FONT = ImageFont.truetype('/Users/user/Dev/custom_postcard/myFont.otf', 67)
    ITALIC_FONT = ImageFont.truetype('/Users/user/Dev/custom_postcard/italic.ttf', 55)
    MESSAGE_SPACE = 15
    ADDRESS_SPACE = 69
    COLOR = (49, 128, 155)

    # pixel placement of text on image
    ADDRESS_X = 1442
    ADDRESS_Y = 662
    NAME_X = 121
    NAME_Y = 130
    MESSAGE_X = 155
    MESSAGE_Y = 204

    # splitter in message string
    SPLIT_ON = 'GIFT'

    # get message data
    messages = {}
    with open('messages.csv') as messages_file:
        messages_reader = csv.reader(messages_file, delimiter=',')
        for row in messages_reader:
            messages[row[0]] = row[1]

    # create images from data
    with open('people_gifts.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count = 1
            else:
                name = row[0]
                gift = row[1]
                category = row[2]
                street = row[4]
                city = row[5]
                state = row[6]
                zipcode = row[7]
                country = row[8]

                line_count += 1

                # get message
                split_message = []
                for m in messages:
                    if m == category:
                        # split message string
                        split_message = messages[m].split(SPLIT_ON)
                # insert gift variable
                message = ''
                if split_message:
                    message = split_message[0]
                    if len(split_message) > 1:
                        message += gift + split_message[1]

                # combine address
                if city is not "":
                    address = name + '\n' + street + '\n' + city + ', ' + state + '\n' + zipcode + ' ' + country
                else:
                    address = name

                # create image
                copy = IMAGE.copy()
                draw = ImageDraw.Draw(copy)

                # wrap text with character width
                wrapper = textwrap.TextWrapper(width=31)
                word_list = wrapper.wrap(text=message)
                wrap_message = ''
                for word in word_list:
                    wrap_message += '\n' + word

                # get width and height of address text to center in placement
                width, height = draw.textsize(address, SMALL_FONT)
                position = ((ADDRESS_X-(width/2)), ADDRESS_Y)

                # place text on image
                draw.text(xy=(NAME_X, NAME_Y), text=name, fill=COLOR, font=BIG_FONT)
                draw.text(xy=(MESSAGE_X, MESSAGE_Y), text=wrap_message, fill=COLOR, spacing=MESSAGE_SPACE, align='center', font=ITALIC_FONT)
                draw.text(xy=position, text=address, fill=COLOR, spacing=ADDRESS_SPACE, align='center', font=SMALL_FONT)

                # save under receiver name
                file_name = name.replace(" ", "_") + '.png'
                copy.save(file_name)

        print(f'Created {line_count-1} images.')


create_custom_postcard()
