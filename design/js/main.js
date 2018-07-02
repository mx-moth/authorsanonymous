/*
	Solid State by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/
import $ from 'jquery';
import { Menu } from './menu';
import { NewsletterForm } from './newsletter';
import { ContactForm } from './contact';

$(function() {
	new Menu($('#menu'), $('body'));

	NewsletterForm.fromElement($('#newsletter'));
	ContactForm.fromElement($('#contact'));
});
