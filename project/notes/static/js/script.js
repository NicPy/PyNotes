$('.action-tch').click(function(){
    console.log(this.dataset.href)
    $('.action-tch').removeClass('active-grey');
    $(this).addClass('active-grey');
    $('.action-section form').addClass('hidden');
    $('.action-section .all-notes-heading span ').attr('class', 'glyphicon glyphicon-plus-sign');
    $('.action-section .all-notes-heading').addClass('add-note');
    $('#ajax-note').removeClass('hidden');
    $('#ajax-note').load(this.dataset.href);
 });

$('.action-section .all-notes-heading').click(function(){
    $('#ajax-note').addClass('hidden');
    $('.action-section form').removeClass('hidden');
    $('.action-section .all-notes-heading').removeClass('add-note');
    $('.action-section .all-notes-heading span ').attr('class', 'glyphicon glyphicon-list-alt');

});

$('.folders-section .repr').click(function(){


    $(this).find('+ .wrapper').slideToggle( "slow", function(){

    });

    var classs = $(this).find(' span').attr('class');
    if (classs == 'glyphicon glyphicon-folder-close'){
        $(this).find('span').attr('class', 'glyphicon glyphicon-folder-open');
    }else{
            $(this).find('span').attr('class', 'glyphicon glyphicon-folder-close');

    };

});

$(function() {
  $("#top-search").autocomplete({
    source: "/notes/api/get_search/",
    minLength: 2,
  });

});