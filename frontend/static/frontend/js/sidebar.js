$(function () {
  setWidthCollapse();
  $('.collapse-sidebar').click(clickCollapse);
  activeSideBar();
});

function setWidthCollapse() {
  if (localStorage.getItem('sidebar') === null) {
    window.localStorage.setItem('sidebar', 'full')
    fullSidebar();
  } else {
    if (localStorage.getItem('sidebar') === 'full') {
      fullSidebar();
    }
    if (localStorage.getItem('sidebar') === 'mini') {
      miniSidebar();
    }
  }

}

function clickCollapse() {
  if ($("#sidebar").hasClass('sidebar-small')) {
    fullSidebar();
  } else {
    miniSidebar();
  }
}

function miniSidebar() {
  window.localStorage.setItem('sidebar', 'mini');
  $("#sidebar").addClass('sidebar-small');
  $("#sidebar").css("width", "50px");
  $(".collapse-sidebar").css("width", "50px");
  $(".content").css("width", "calc(100% - 50px)");
}

function fullSidebar() {
  window.localStorage.setItem('sidebar', 'full');
  $("#sidebar").removeClass('sidebar-small');
  $("#sidebar").css("width", "280px");
  $(".collapse-sidebar").css("width", "280px");
  $(".content").css("width", "calc(100% - 280px)");
}

function activeSideBar() {
  var path = window.location.pathname;
  $(".item-sidebar").each(function () {
    if ($(this).hasClass('active')) {
      $(this).removeClass('active');
    }
    if (path.length === 1) {
      $('#dashboard_item').addClass('active');
    }
    var dataId = $(this).attr('data-id');
    if (path.substring(0, dataId.length) === dataId) {
      $(this).addClass('active');
    }
  });
}
