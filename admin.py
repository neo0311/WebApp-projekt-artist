from numpy import delete
import streamlit as st

def maintain(layout_data=None):

    """
    Renders the 'Lab' page.

    Parameters
    ----------

    layout_data: config data for rendering page.

    """
    user = st.sidebar.text_input('Username')
    passwd = st.sidebar.text_input('Password', type='password')

    if (user in [layout_data["username_artist"], layout_data["username_newt"]] 
            and passwd in [layout_data["passwd_artist"], layout_data["passwd_newt"]]):

        st.title(body='🔧 Maintenence 🔨')
        st.subheader(body=("Ahh, so you made it to the admin page, huh?. 😉" + 
                            "\nWell let's get creative! 😎"))
        action = st.selectbox(label='What do you want to do?', 
                                options=('Nothing much, just having a look 😏',
                                'Edit page layout ✔', 'Upload something ▲', 
                                'Delete something ❌', 'Self Destruct 💣💀'))
        
        if action=='Nothing much, just having a look 😏':
            st.info("The page gives you complete access. You can even delete the whole "
                    "page if you want. But unless that is not your intention, just don't "
                    "click any 'confirm' buttons or type 'yes' anywhere. Other than that "
                    "it is perfectly safe to go anywhere, even to the 'Self Destruct' option. "
                    "Just have a look around. 😉")
            st.info("One last thing. If you leave this 'Lab' page in between editing data, "
                    "for eg. to see your wonderful drawings again, you have to "
                    "log in to this page again. So, save before you leave.")
            with st.beta_expander("Wanna see the machinery behind all this??"):
                st.write(("Okey, so go to the following link."))
                st.write("[Code (the boring stuff)](www.google.com)")
                st.write("So, there will be many files. But, don't panic! "
                         "The '.py' files are the actual codes. The "
                         "'resources' folder contains all the image "
                         "and layout data needed to run the web app.")

        elif action=='Upload something ▲':
            uploader(layout_data)
        elif action=='Edit page layout ✔':
            editor(layout_data, user=user)
        elif action=='Delete something ❌':
            delete(layout_data)
        elif action=='Self Destruct 💣💀':
            exterminate()
    
    elif user=='' or passwd=='':
        pass
    else:
        st.sidebar.error('Sorry not for you! 😐 or maybe just wrong password!')


def uploader(layout_data):
    """
    Renders the upload functionality

    Paramters
    ---------

    layout_data: config data for rendering page.

    """
    st.header('Uploader')
    upload_type = st.selectbox(label='Choose what you want to uplaod:', 
                            options=(layout_data["sidebar_drawings"], 
                                    layout_data["sidebar_stencils"], 
                                    layout_data["sidebar_photos"], 
                                    layout_data["sidebar_writings"], 
                                    layout_data["sidebar_others"]))

    if upload_type==layout_data["sidebar_drawings"]:
        st.text(body='Ah, classy!!')
        folder = 'drawings'
    elif upload_type==layout_data["sidebar_stencils"]:
        st.text(body='People!, most are mean, but the stencils are sweet')
        folder = 'stencils'
    elif upload_type==layout_data["sidebar_photos"]:
        st.text(body='Moments!, Frozen in time.')
        folder = 'photos'
    elif upload_type==layout_data["sidebar_writings"]:
        st.text(body='Thoughts!, do it before the next passes through your head.')
        folder = 'writings'
    elif upload_type==layout_data["sidebar_others"]:
        st.text(body="Seriously Lady!!, you don't even know what you are dong?😐 "  
                "\nWell, welcome to the club! 😉")
        folder = 'others'
    
    #uploader
    file = st.file_uploader(label='Upload file')
    if file is not None:
        save_uploadedfile(file=file, folder=folder)

def editor(layout_data,user=None):

    """
    Renders editor part of the page.

    Paramters
    ---------

    layout_data: config data for rendering page.

    """
    import json
    import os
    st.header('Editor')
    st.text("Okey, so you don't like my content? This is sad. "
                "\nJust Kidding! Go, pour those words in!!")
    with st.beta_expander("🌟🌟Here!!, The secret to all "
                            "of life's problems!!🌟🌟"):
        st.write("Sorry, this was the only way to make sure "
                "you read this.😁\nJust select an option " 
                "from the drop down menu and start editing!!. "
                "Some texts may contain weird language like :'sunglasses':. " 
                "\nDon't worry, they are just for adding emojis. Just leave "
                "them and edit the rest of text or if you don't want them around, "
                "delete those parts from text. If you like them and want to " 
                "replace them with a seperate one, go to the below link and "
                "replce the text in between :'text':" )
        st.write("Phew, happy editing!!!")

        st.write("[Emoji aliases](https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json)")
    edit_option = st.selectbox(label="What do you want to edit?", 
                    options=(layout_data["sidebar_home"] + ' page', 
                    layout_data["sidebar_drawings"] + ' page', 
                    layout_data["sidebar_stencils"] + ' page', 
                    layout_data["sidebar_photos"] + ' page', 
                    layout_data["sidebar_writings"] + ' page',
                    "Sidebar", "Page Settings", "Username and Password"))

    edited_values ={}
    if edit_option==layout_data["sidebar_home"] + ' page':
        
        edited_values["home_title"] = st.text_input(label="The title", 
                                        value=layout_data["home_title"])
        edited_values["home_subheader"] = st.text_input(label="The following text", 
                                        value=layout_data["home_subheader"])
        
        if os.path.isfile('resources'+os.sep+'home.jpeg'):
            
            home_action = st.radio('Change home page cover picture?', 
                             options=("No, it's Ok.", "Change", "Delete"))
            if home_action=="Change":
                st.image('resources'+os.sep+'home.jpeg', 'Current home cover picture', width=500)
                home_img = st.file_uploader('Upload new home cover picture')
                if home_img is not None:
                    with open(os.path.join('resources'+
                        os.sep+'home.jpeg'),"wb") as home_file:
                        home_file.write(home_img.getbuffer())
                        home_file.close()
                        st.success("Success!. Saved file, " )
                        st.warning('Remove the uploaded file from list by clicking ' +
                            'the cross button if the file has been uploaded correctly!')
            elif home_action=="Delete":
                st.image('resources'+os.sep+'home.jpeg', 'Current home cover picture', width=500)
                home_img_remove = st.button('Sure?')
                if home_img_remove:
                    if os.path.isfile('resources'+os.sep+'home.jpeg'):
                        os.remove('resources'+os.sep+'home.jpeg')
                        st.success('Done, rerun the page.')
        else:
            add_home_cover = st.radio("Add a home cover picture?", options=('No', 'Yes!'))
            if add_home_cover=='Yes!':
                home_img = st.file_uploader('Upload new home cover picture')
                if home_img is not None:
                    with open(os.path.join('resources'+
                        os.sep+'home.jpeg'),"wb") as home_file:
                        home_file.write(home_img.getbuffer())
                        home_file.close()
                        st.success("Success!. Saved file, " )
                        st.warning('Remove the uploaded file from list by clicking ' +
                            'the cross button if the file has been uploaded correctly!')

    elif edit_option==layout_data["sidebar_drawings"] + ' page':
        edited_values["drawings_title"] = st.text_input(label="The title", 
                                        value=layout_data["drawings_title"])
        edited_values["drawings_subheader"] = st.text_input(label="The following text", 
                                        value=layout_data["drawings_subheader"])
    elif edit_option==layout_data["sidebar_stencils"] + ' page':
        edited_values["stencils_title"] = st.text_input(label="The title", 
                                        value=layout_data["stencils_title"])
        edited_values["stencils_subheader"] = st.text_input(label="The following text", 
                                        value=layout_data["stencils_subheader"])
    elif edit_option==layout_data["sidebar_photos"] + ' page':
        edited_values["photos_title"] = st.text_input(label="The title", 
                                        value=layout_data["photos_title"])
        edited_values["photos_subheader"] = st.text_input(label="The following text", 
                                        value=layout_data["photos_subheader"])
    elif edit_option==layout_data["sidebar_writings"] + ' page':
        edited_values["writings_title"] = st.text_input(label="The title", 
                                        value=layout_data["writings_title"])
        edited_values["writings_subheader"] = st.text_input(label="The following text", 
                                        value=layout_data["writings_subheader"])
    elif edit_option==layout_data["sidebar_others"] + ' page':
        edited_values["writings_title"] = st.text_input(label="The title", 
                                        value=layout_data["others_title"])
        edited_values["others_subheader"] = st.text_input(label="The following text", 
                                        value=layout_data["others_subheader"])
    elif edit_option=="Username and Password":
        user_to_edit = st.radio("Choose a user to edit", options=('Not editing',layout_data["username_newt"], 
                            layout_data["username_artist"]))
        if user_to_edit==user:
            if user==layout_data["username_artist"]:
                edited_values["username_artist"] = st.text_input(label='New username',
                                                        value=user_to_edit)
                edited_values["passwd_artist"] = st.text_input(label='New username',
                                                        value=layout_data["passwd_artist"])
            elif user==layout_data["username_newt"]:
                edited_values["username_newt"] = st.text_input(label='New username',
                                                        value=user_to_edit)
                edited_values["passwd_newt"] = st.text_input(label='New username',
                                                        value=layout_data["passwd_newt"])
        elif user_to_edit not in [user, "Not editing"]:
            st.error('Not fair you selfish person!! 😐')
                
    elif edit_option=="Sidebar":
        edited_values["sidebar_text"] = st.text_input(label="Sidebar text", 
                                        value=layout_data["sidebar_text"])
        edited_values["sidebar_choice"] = st.text_input(label="Sidebar choice text", 
                                        value=layout_data["sidebar_choice"])
        
        #st.subheader("Page names on sidebar list")
        with st.beta_expander("Page names on sidebar list"):
            edited_values["sidebar_home"] = st.text_input(
                        label=layout_data["sidebar_home"]+ ' page', 
                                value=layout_data["sidebar_home"])
            edited_values["sidebar_drawings"] = st.text_input(
                        label=layout_data["sidebar_drawings"]+ ' page', 
                            value=layout_data["sidebar_drawings"])
            edited_values["sidebar_stencils"] = st.text_input(
                        label=layout_data["sidebar_stencils"]+ ' page', 
                            value=layout_data["sidebar_stencils"])
            edited_values["sidebar_photos"] = st.text_input(
                        label=layout_data["sidebar_photos"]+ ' page', 
                            value=layout_data["sidebar_photos"])
            edited_values["sidebar_writings"] = st.text_input(
                        label=layout_data["sidebar_writings"]+ ' page', 
                            value=layout_data["sidebar_writings"])
            edited_values["sidebar_others"] = st.text_input(
                        label=layout_data["sidebar_others"]+ ' page', 
                            value=layout_data["sidebar_others"])
            edited_values["sidebar_admin"] = st.text_input(
                        label=layout_data["sidebar_admin"]+ ' page', 
                            value=layout_data["sidebar_admin"])

    elif edit_option=="Page Settings":
        edited_values["settings_nColumns"] = st.number_input(
                        label="The number of pictures in each row of the gallery",
                            value=layout_data["settings_nColumns"])
        edited_values["settings_wide"] = st.radio(
                        label=("Adapt the page for wide screens or.."), 
                            options=("wide", "centered"))
    
    save = False
    reset = False
    save = st.button('Save settings? ✔')
    reset = st.button('Reset to default? ⚠')
    if save:
        for key in edited_values.keys():
            layout_data[key] = edited_values[key]
            new_data_file = open("resources" + os.sep + "data.json", "w")
            json.dump(layout_data, new_data_file)
            new_data_file.close()

    if reset:
        old_data_file = open("resources" + os.sep + "data_default.json", "r")
        old_layout_data = json.load(old_data_file)
        old_data_file.close()

        new_data_file = open("resources" + os.sep + "data.json", "w")
        json.dump(old_layout_data, new_data_file)
        new_data_file.close()

        import shutil
        shutil.copyfile('resources'+os.sep+'home_default.jpeg', 'resources'+os.sep+'home.jpeg')

def delete(layout_data):
    from main import read_imgs, arrange_imgs
    import os
    st.text("Okey, so you want to destroy stuff huh? 😪"
            "\nIs Hulk your uncle? 😈\nFYI, we can't afford a recycle bin. So, be careful! 😑")
    to_delete = st.selectbox(label='What do you want to delete?.', 
                    options=('Nothing. Changed my mind! 😪', layout_data["sidebar_drawings"], 
                    layout_data["sidebar_stencils"], layout_data["sidebar_photos"], 
                    layout_data["sidebar_writings"], layout_data["sidebar_others"]))

    if to_delete not in ['Nothing. Changed my mind! 😪']:
        st.info("Remember the picture numbers you want to delete and enter "
                "them below seperated by commas, eg. 1,5,6 or \ntype all to delete all files. "
                "Then click rerun on the top right menu of the page.")
        if to_delete==layout_data["sidebar_drawings"]:
            path='resources' + os.sep + 'drawings' + os.sep + '*.*'
            
        elif to_delete==layout_data["sidebar_stencils"]:
            path='resources' + os.sep + 'stencils' + os.sep + '*.*'

        elif to_delete==layout_data["sidebar_photos"]:
            path='resources' + os.sep + 'photos' + os.sep + '*.*'

        elif to_delete==layout_data["sidebar_others"]:
            path='resources' + os.sep + 'others' + os.sep + '*.*'

        imgs, image_files = read_imgs(path=path, return_names=True)
        arrange_imgs(image=imgs, st=st, layout_data=layout_data, caption=True)
        pictures_to_delete = st.text_input('Enter the pictures you want to delete:')
        delete_confirm=False
        delete_confirm = st.button('Confirm')
        if delete_confirm:
            if pictures_to_delete=='all':
                for file in image_files:
                    os.remove(file)
            else:
                for picture_id in pictures_to_delete:
                    os.remove(image_files[int(picture_id)-1])

def exterminate():

    """
    Exterminates all code of this project. Literally!

    """
    import shutil
    import os
    st.warning("Okey, so you want to do this huh? Go ahead. " 
                "Just to rephrase the title,  this will delete "
                "everything of this page as you know it. One last quesion. "
                "\nDoes the name 'Thanos' sound familier to you?")
    exterminate_confirm_text = st.text_input('So, are you sure?? 😢. Then type yes')
    exterminate_confirm_button = st.button('Exterminate!!')

    if exterminate_confirm_text=='yes' and exterminate_confirm_button:
        directory_list = os.listdir('.')
        if __name__+'.py' in directory_list:
            for object_ in directory_list:
                if os.path.isdir(object_) and not object_.startswith('.'):
                    shutil.rmtree(object_)
                elif os.path.isfile(object_):
                    os.remove(object_)
            st.error('DONE😢')


def save_uploadedfile(file=None, folder=''):
    """
    Saves the uploaded file to respective folder.

    Paramters
    ---------

    file: BytesIo object from streamlit uploader.

    folder: folder name
    """
    import os
    with open(os.path.join('resources'+
                os.sep+folder,file.name),"wb") as f:
         f.write(file.getbuffer())
         f.close()
         st.success("Success!. Saved file, " +
                    "{} to {}".format(file.name, folder))
         st.warning('Remove the uploaded file from list by clicking ' +
                    'the cross button if the file has been uploaded correctly!')