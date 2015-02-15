var old_u = '';

function view_movie(u)
{

	//@credit: http://www.longtailvideo.com/blog/26517/using-the-browsers-new-html5-fullscreen-capabilities/
    var element = document.getElementById('ifr_dl');
    if (element.mozRequestFullScreen) {
      element.mozRequestFullScreen();
    } else if (element.webkitRequestFullScreen) {
      element.webkitRequestFullScreen();
   }
	$('ifr_dl').src=u;
	$('spn_dl').style.display='block';$('body_content').style.visibility='hidden';   
}
function show_dl(u)
{window.open(u);}
function close_dl()
{$('spn_dl').style.display='none';$('body_content').style.visibility='';}