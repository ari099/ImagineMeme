'use strict';

/**
 * Main application component
 */
const App = props => {
    const [image, setImage] = React.useState(null);
    const [topText, setTopText] = React.useState("");
    const [bottomText, setBottomText] = React.useState("");
    const [memeImage, setMemeImage] = React.useState(null);
    const showImage = e => {
        setImage(e.target.files[0]);
        setMemeImage(null);
    }
    const uploadFormData = e => {
        if(image !== null && topText !== "" && bottomText !== "") {
            const formData = new FormData();
            formData.append(
                "img-upload",
                image
            );
            formData.append(
                "top-text",
                topText
            );
            formData.append(
                "bottom-text",
                bottomText
            );

            // Upload the information
            axios.post("/imagine/", formData, { responseType: "blob" }).then(response => {
                setMemeImage(URL.createObjectURL(response.data));
            })
        }
    }
    return (
        <>
            <form className="imgmm-form">
                <div className="form-group">
                    <label htmlFor="file-upload">Upload your Photo: </label>
                    <input id="file-upload"
                        className="imgmm-file-upload"
                        type="file" onChange={showImage} /><br />
                    <img className="imgmm-img" src={(image === null) ? image : window.URL.createObjectURL(image)} />
                </div>
                <div className="form-group">
                    <label htmlFor="top-textbox">Meme Top Text: </label>
                    <input id="top-textbox"
                        className="imgmm-textbox form-control"
                        placeholder="Enter your top text here...."
                        onChange={e => setTopText(e.target.value)} />
                    {topText === "" && <small id="top-textbox-help" className="form-text text-muted">Every meme needs a top text!</small>}
                </div>    
                <div className="form-group">
                    <label htmlFor="bottom-textbox">Meme Bottom Text: </label>
                    <input id="bottom-textbox"
                        className="imgmm-textbox form-control"
                        placeholder="Enter your bottom text here...."
                        onChange={e => setBottomText(e.target.value)} />
                    {bottomText === "" && <small id="bottom-textbox-help" className="form-text text-muted">Every meme needs a bottom text too!</small>}
                </div>
            </form>
            <button className="imgmm-btn btn btn-success"
                onClick={uploadFormData}>Create Meme</button>
            <img className="imgmm-img" src={memeImage} />
        </>
    );
};

ReactDOM.render(
   <App />,
   document.getElementById("root")
);
