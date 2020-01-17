import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppComponent} from './app.component';
import {FormsModule} from '@angular/forms';
import {PostFormComponent} from './post-form/post-form.component';
import {PostComponent} from './post/post.component';

@NgModule({
  declarations: [
    AppComponent,
    PostFormComponent,
    PostComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
