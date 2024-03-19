$(document).ready(()=> {
  // 获取当前路由
  let currentRoute = window.location.pathname;
  console.log(currentRoute)
  // 移除所有元素的is-active类
  $('.bd-navbar-item').removeClass('is-active');

  // 检查当前路由并添加相应的class
  if (currentRoute === '/') {
    $('.bd-navbar-item-home').addClass('is-active');
  } else if (currentRoute === '/baike') {
    $('.bd-navbar-item-love').addClass('is-active');
  } else if (currentRoute === '/predict') {
    $('.bd-navbar-item-images').addClass('is-active');
  }
  // 控制折叠菜单的点击事件
  $(".navbar-burger").click(()=> {
      $(".navbar-burger").toggleClass("is-active");
      $(".navbar-menu").toggleClass("is-active");
  });

});
