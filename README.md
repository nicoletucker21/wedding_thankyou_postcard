# Wedding Thank You Postcard
Don't want to write and address all of your wedding gift thank you cards by hand? 
Use this python script to automate it, and even customize each card by category and gift!

5 FILES REQUIRED FOR CODE TO RUN CORRECTLY:

1. people_gifts.csv

This file is a list of all the people who gave you a wedding gift, including their full name (couples or family names combined), the item gifted, the category of the gift, and the full mailing address of the gift giver. I recommend using this template from the beginning and keeping track of gifts as you receive them to save time later!

![people_gift template](https://github.com/nicoletucker21/wedding_thankyou_postcard/blob/master/people_gift_template.png)

2. message.csv

This file is a list of all the messages you want printed on your postcards, organized by gift category.
The code is written so that gift data is inserted into the message, so feel free write a specific message for each cateogory and include the word GIFT where you want the gift data inserted!

![message template](https://github.com/nicoletucker21/wedding_thankyou_postcard/blob/master/messages_template.png)

3. font.png (or .jpg)

This file is a photo or design for the front of your postcard. Make sure it is 300 DPI (best resolution for printing). That is 300 pixels per inch if you are designing/exporting the file/photo yourself. The files in my repository are 1275 × 1875 pixels, 4 x 6 inches with a 1/8 inch bleed on each side.

4. back.png (or .jpg)

This file is the photo or design for the back of your postcard. Make sure it is also 300 DPI and same pixel size as your front file.

5. font files (.otf or .ttf)
You can use as many fonts as you want. You will be able to import them, determine the size, alignment, and color of each font. Since you are creating a custom postcard, get creative. Google for sites that have many beautiful and free fonts you can download!

Make sure all of these files are in the same directory folder as your script file!

At the top of the function, there are constants that can be updated. The trickiest part of the code is getting the correct placement on the back for the text you want written. The X and Y placement is determined by number of pixels, it will take some trial and error to get the text just where you want it depending on your back.png design.


Once the code runs and creates all of the back images, you can take the files to a custom printer to get it printed (I printed it at my university campus print shop, they were able to accomodate the same front and 160 unique backs for each print). You could also upload all the images to a Photo Center account (Such as Costco, Walmart, Staples, etc) and pair the front and back for each print if you can't find a custom print shop that can accomodate your print request.

That's it! I hope it saves you some headache, time, and handing cramping. Let me if you have any questions. Good luck!
