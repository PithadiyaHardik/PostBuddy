function postPreview(input) {
  let img = input.files[0];
  let image_label = document.getElementById("postImage");

  let url = URL.createObjectURL(img);
  image_label.src = url;
}
