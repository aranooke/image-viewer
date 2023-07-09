import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
class App:
     def __init__(self) -> None:
          # Specify the path to your image file
        
        image_path = 'path/to/your/image.jpg'
        # Create the Tkinter root window
        self.root = tk.Tk()
        
        open_button = tk.Button(text="Open image",
                                command = self.open_file);

        color = tk.Button(text = "Make black color image" );
        rotate = tk.Button(text="Rotate 90 image");

        # color.pack(side=tk.LEFT,padx= 5);
        # rotate.pack(side=tk.LEFT,padx= 5);
        open_button.pack(padx=30,pady=30);

        # Create an instance of the ImageViewer class
        # image_viewer = ImageViewer(root, image_path)
        
        # Start the Tkinter event loop
        self.root.mainloop()





     def open_file(self):
        filename = filedialog.askopenfile();
        image_formats = [".png",".jpeg",".jpg"];
        if any(filename.name.lower().endswith(i) for i in image_formats):
                print(filename.name);
                image_viewer = ImageViewer(self.root,filename.name);
                
        else:
            messagebox.showinfo("Error","Its not image,try again ");



class ImageViewer:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Image Viewer")
        
        # Load the image
        self.image = Image.open(image_path)
        self.image.thumbnail((800, 600))  # Resize the image
        
        # Create a Tkinter-compatible photo image
        self.photo = ImageTk.PhotoImage(self.image)
        
        # Create a label to display the image
        self.label = tk.Label(self.root, image=self.photo)
        self.label.pack()
        
        # Bind the 'q' key to quit the application
        self.root.bind('q', lambda event: self.root.quit())
    def rotate(self):
        rotated_img     = self.image.rotate(90);
    def toBlackWhite(self):
        black_white_img = self.image.convert('L');


if __name__ == '__main__':
    app = App();
