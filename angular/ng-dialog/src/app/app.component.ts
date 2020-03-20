import {Component} from '@angular/core';
import {MatDialog} from '@angular/material/dialog';
import {DialogMenuComponent} from './dialog-menu/dialog-menu.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  private id: number;
  private title: string;

  constructor(private dialog: MatDialog) {
    this.id = 1;
    this.title = 'default';
  }

  openDialog(): void {
    let dialogRef = this.dialog.open(DialogMenuComponent, {data: {id: this.id, title: this.title}});
    dialogRef.afterClosed().subscribe(value => {
      this.id = parseInt(value.id);
      this.title = value.title;
      console.log('Data dispatched from the form (id, title):');
      console.log(this.id);
      console.log(this.title);
    });
  }
}
