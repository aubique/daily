import {Component, OnInit} from '@angular/core';
import {Observable} from "rxjs";

export interface Post {
  title: string;
  text: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  subscribeDate: Date;
  initialDate: Date = new Date();

  posts: Post[] = [
    {title: 'Beer', text: 'The best beer in the world'},
    {title: 'Bread', text: 'The best bread'}
  ]
  search: string = '';
  searchField: string = 'title';

  addPost() {
    this.posts.unshift({
      title: 'Angular 8',
      text: 'Course'
    })
  }

  p: Promise<string> = new Promise<string>(resolve => {
    setTimeout(() => {
      resolve('Promise Resolved')
    }, 4000)
  });

  observableDate$: Observable<Date> = new Observable<Date>(obs => {
    setInterval(() => {
      obs.next(new Date());
    }, 1000)
  });

  ngOnInit(): void {
    this.observableDate$.subscribe(date => {
      this.subscribeDate = date;
    })
  }

}
