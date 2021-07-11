
import streamlit as st
import os
import json

def start():

    """
    The main function that renders the app.
    """
    #loading the webapp layout data
    data_file = open("resources" + os.sep + "data.json", "r")
    layout_data = json.load(data_file)
    data_file.close()

    #rendering the page
    st.set_page_config(layout=layout_data["settings_wide"])

    #sidebar
    st.sidebar.write(layout_data["sidebar_text"])
    select = st.sidebar.selectbox(label=layout_data["sidebar_choice"], 
            options=(layout_data["sidebar_home"], layout_data["sidebar_drawings"], 
            layout_data["sidebar_stencils"], layout_data["sidebar_photos"], 
            layout_data["sidebar_writings"], layout_data["sidebar_others"],
            layout_data["sidebar_admin"]))
    
    #sidebar selector
    if select == layout_data["sidebar_home"]:
        from home import home
        home(layout_data)
    elif select == layout_data["sidebar_drawings"]:
        from drawings import show_drawings
        show_drawings(layout_data=layout_data)
    elif select == layout_data["sidebar_stencils"]:
        from stencils import show_stencils
        show_stencils(layout_data=layout_data)
    elif select == layout_data["sidebar_photos"]:
        from photos import show_photos
        show_photos(layout_data=layout_data)
    elif select == layout_data["sidebar_writings"]:
        from writings import show_writings
        show_writings(layout_data=layout_data)
    elif select == layout_data["sidebar_others"]:
        from others import show_others
        show_others(layout_data=layout_data)
    elif select == layout_data["sidebar_admin"]:
        from admin import maintain
        maintain(layout_data)

def read_imgs(path=str, return_names=False):

    """
    Reads images from the respective path.

    Parameters
    ----------

    path: path to the folder containing images.

    return_names: returns a list of image file names if set True.

    """
    import cv2
    import glob
    imgs = []
    for image in glob.glob(path):
        img1 =cv2.imread(image)
        img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) #changes to RGB
        imgs.append(img)
    
    if return_names:
        return imgs, glob.glob(path)
    else:
        return imgs

def arrange_imgs(image=None, st=None, layout_data=None,
                 caption=None):
    
    """
    Arranges images on the page.

    Parameters
    ----------

    image: list of images to be rendered.

    st: streamlit object

    layout_data: dictionary with info about the layout of page

    caption: Numbers the images if set True.

    """
    Ncolumns = layout_data["settings_nColumns"]
    range_ = len(image) + 2*Ncolumns 
    cols = st.beta_columns(Ncolumns)
    for i in range(0, range_, Ncolumns):
        for j in range(0,Ncolumns):
            if (i+j)<len(image):
                if caption:
                    caption=str(i+j+1)
                cols[j].image(image=image[i+j], use_column_width=True, 
                                caption=caption)

if __name__ == "__main__":
    start()