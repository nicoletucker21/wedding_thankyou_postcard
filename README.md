# Wedding Thank You Postcard
Don't want to write and address all of your wedding gift thank you cards by hand? 
Use this python script to automate it, and even customize each card by category and gift!

FILES REQUIRED FOR CODE TO RUN CORRECTLY:

1. people_gifts.csv

This file is a list of all the people who gave you a wedding gift, including their full name (couples or family names combined), the item gifted, the category of the gift, and the full mailing address of the gift giver.

![people_gift template](https://github.com/nicoletucker21/wedding_thankyou_postcard/blob/master/people_gift_template.png)

<img
src="https://github.com/nicoletucker21/wedding_thankyou_postcard/blob/master/people_gift_template.png"
raw=true
alt="people_gift template"
style="margin-right: 10px;"
/>

2. message.csv

This file is a list of all the messages you want printed on your postcards, organized by gift category.
The code is written so that gift data is inserted into the message, so feel free write a specific message for each cateogory and include the word GIFT where you want the gift data inserted!

![message template](https://github.com/nicoletucker21/wedding_thankyou_postcard/message_template.png)

3. font.png (or .jpg)

This file is a photo or design for the front of your postcard. Make sure it is 300 DPI (best resolution for printing). That is 300 pixels per inch if you are designing the file yourself.

4. back.png (or .jpg)

This file is the photo or design for the back of your postcard. Make sure it is also 300 DPI.

5. font files (.otf or .ttf)
You can use as many fonts as you want. You will be able to import them, determine the size, alignment, and color of each font.


At the Top of the function, there are constants that can be updated. The trickiest part of the code is getting the correct placement for the text you want written. The X and Y placement is determined by number of pixels, it will take some trial and error to get the text just where you want it depending on your back.png design.


