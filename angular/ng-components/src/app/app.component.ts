import {Component, OnInit} from '@angular/core';

export interface Post {
  title: string;
  text: string;
  id?: number;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {

  posts: Post[] = [
    {title: 'I wanna learn Angular components', text: 'I\'m still learning components', id: 1},
    {title: 'Next block', text: 'Directives', id: 2}
  ];

  ngOnInit(): void {
    setTimeout(() => {
      console.log('Timeout');
      this.posts[0] = {
        title: 'Changed',
        text: 'new text',
        id: 33
      };
    }, 5000);
  }

  updatePosts(post: Post) {
    this.posts.unshift(post);
  }

  removePost(id: number) {
    console.log('Id to remove: ' + id);
    this.posts = this.posts.filter(p => p.id !== id);
  }
}
