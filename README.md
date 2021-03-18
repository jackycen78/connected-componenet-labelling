# connected-component-labelling

Connected-component labelling groups pixels based on their pixel intensity and connectivity with neighbouring pixels. Once all the groups have been identify, they are assigned different colours/shades, resulting in distinct groups of connected components. The algorithm goes as,

1. Find the gradients of the image
2. Start with label 0
3. Check every pixel from top left to bottom right
    - if pixel has non-zero gradient value and not labelled
      - assign current label to pixel
      - create queue
      - add the 8 direct neighbouring pixels of current pixel in queue
      - while queue is not empty:
         - if pixel has non-zero gradient value and not labelled
            - assign current label to pixel
            - add neighouring pixels to queue
    - increase label by 1
 
 



Original Image:

![image](https://user-images.githubusercontent.com/24669054/111684101-a7b38300-87fc-11eb-9352-7d4f5d817f76.png)

Gaussian Blur:

![image](https://user-images.githubusercontent.com/24669054/111677219-62d81e00-87f5-11eb-804f-266f145a89a1.png)

Edge Detection:

![image](https://user-images.githubusercontent.com/24669054/111677364-8733fa80-87f5-11eb-80ca-d3a9e146802c.png)

Thresholding:

![image](https://user-images.githubusercontent.com/24669054/111677369-88652780-87f5-11eb-912a-27cfffa9039d.png)

Connected-components:

![image](https://user-images.githubusercontent.com/24669054/111679140-5ead0000-87f7-11eb-99ef-0f330f6f2eb0.png)
