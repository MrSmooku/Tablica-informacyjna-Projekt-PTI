﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Tablica.Controllers {
    public class HomeController : Controller {
        public ActionResult Index() {
            return View();
        }

        public ActionResult About() {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact() {
            ViewBag.Message = "Your contact page.";

            return View();
        }
        public ActionResult Widok() {
            ViewBag.Message = "Przykładowy widok";
            return View();
        }
        public PartialViewResult GetInfo() {
            ViewBag.ItemDetails = "Jakiej info, nie wiem jakie";
            return PartialView("_JakiesInfo");
        }
    }
}