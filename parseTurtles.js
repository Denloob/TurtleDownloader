/*
Usage:
open https://emojiturtledaily.tumblr.com/archive
press ctrl+shift+i to open the inspector and change the tab to "Console"
paste the code into the console
press midle mouse button on the website and scroll down to the bottom of the site
in the console type: JSON.stringify(image_links)
copy the result and save it as a turtles.json file
*/

const image_links = [];

function get_url(img_element) {
  const srcset = img_element[i].getAttribute("srcset");
  console.log(srcset);
  const src = srcset.split(",")[0].split(" ")[0];
  return src;
}

setInterval(() => {
  const img_tag = document.getElementsByClassName("BIv_s");
  for (var i = 0; i < img_tag.length; i++) {
    const url = get_url(img_tag[i]);
    if (!image_links.includes(url)) image_links.push(url);
  }
}, 10);
