function addfollowers(input) {
  let account = input.getAttribute("name");
  let follower = input.getAttribute("username");
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/addFollowers");
  xhr.responseType = "json";
  let data1 = {
    accountHolder: account,
    folllowerUsername: follower,
  };
  xhr.send(JSON.stringify(data1));
  input.value = "Following";
  input.disabled = true;
}
