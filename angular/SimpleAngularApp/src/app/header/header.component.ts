import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor() {
  }

  pageRequested = 1;

  ngOnInit() {
  }

  onPageMethod(page) {
    this.pageRequested = page;
    console.log(this.pageRequested);
  }

}
