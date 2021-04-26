function removeResponse(issueId, csrfToken){
    $.post(`/api/post/removeResponse/`,
      {
          issue_id: issueId, 
          csrfmiddlewaretoken: csrfToken
      },
        function( data ) {
          if (data.status === 'success'){
            $('#assign_alert').addClass("show");
            setTimeout(() => {  $('#assign_alert').removeClass("show"); }, 2000);
            $(`.row_${issueId}`).hide();
          }
      });
  };