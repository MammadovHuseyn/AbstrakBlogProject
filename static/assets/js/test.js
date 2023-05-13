function addComment(comment) {
    const commentDiv = document.createElement('div');
    commentDiv.classList = "comment"

    const thumbnailDiv = document.createElement('div');
    thumbnailDiv.classList = "thumbnail"
    
    const thumbnailImg = document.createElement('img');
    thumbnailImg.innerHTML = comment.image.url
    
    const nameSpan = document.createElement('span');
    nameSpan.textContent = comment.name + ': ';
    const textSpan = document.createElement('span');
    textSpan.textContent = comment.comment;
    commentDiv.appendChild(nameSpan);
    commentDiv.appendChild(textSpan);
    commentsDiv.appendChild(commentDiv);
  }
  
// Function to update the comments section with new data
function updateComments(comments) {
commentsDiv.innerHTML = '';
comments.forEach(comment => {
    addComment(comment);
});
}

  <div class="comment">
    <div class="thumbnail">
        <img class='rounded-circle border border-dark' src="{{comment.writer.avatar.url}}"  alt="Blog Comment">
    </div>
    <div class="content">
        <div class="heading">
            <h5 class="title">{% if comment.writer.username == user.username %}You {% else %}{{comment.writer.username}}{% endif %}</h5>
            <div class="comment-date">
                <p>{{comment.created_at|timesince}}</p>
                <a class="reply-btn" href="#"><i class="fas fa-reply"></i></a>
            </div>
        </div>
        <p>{{comment.comment_text}}</p>
    </div>
</div>