$(function () {
  $('.nav-btn').on('click', function () {
    $(this).toggleClass('open');
  });
});

$(document).ready(function () {
  $(window).scroll(function () {
    var scroll = $(window).scrollTop();
    if (scroll > 100) {
      $("#header").addClass('glass-effect');
    } else {
      $("#header").removeClass("glass-effect");
    }
  });

  $(".tab").hover(function () {
    let tabs = $(this).closest('.tabs');
    let tabContent = tabs.siblings('.tab-content');
    let backgroundContainer = tabs.siblings('.background-container');

    // Hapus kelas "active" dari semua tab dan tambahkan ke tab yang dihover
    tabs.find('.tab').removeClass('active');
    $(this).addClass("active");

    // Sembunyikan semua konten dan tampilkan yang sesuai dengan tab yang dihover
    let selectedTab = $(this).data("tab");
    tabContent.find(".content").removeClass("active");
    tabContent.find("#" + selectedTab).addClass("active");

    // Jika ada background-container, perbarui gambar sesuai dengan tab yang aktif
    if (backgroundContainer.length) {
      let bgImage = backgroundContainer.find(".bg-images img#" + selectedTab).attr("src");
      if (bgImage) {
        backgroundContainer.css("background-image", `url(${bgImage})`);
      }
    }
  });


  $('.marquee-container').each(function () {
    const cont = $(this); // Mengambil marquee-container saat ini
    const content = cont.find('.marquee-content');
    const clone = content.clone();
    const clone2 = clone.clone();
    cont.append(clone);
    cont.append(clone2); // Clone hanya untuk container ini

    cont.find('.marquee-content').addClass('marquee'); // Tambahkan class marquee pada konten yang di-clone
  });

  const tabCourse = $('#course-tab');
  const tabDuration = $('#tab-duration');

  let courseActive = tabCourse.find('.tab.active');
  let dataCourseActive = courseActive.data('course');

  let durationActive = tabDuration.find('.tab.active');
  let dataDurationActive = durationActive.data('duration');

  filterClasses(dataCourseActive);
  filterDuration(dataDurationActive);

  tabCourse.find('.tab').on('click', function (e) {
    e.preventDefault();
    let course = $(this).data('course');
    filterClasses(course);
    $(this).addClass('active');
    $(this).siblings().removeClass('active');
  });

  tabDuration.find('.tab').on('click', function (e) {
    e.preventDefault();
    let duration = $(this).data('duration');
    filterDuration(duration);
    $(this).addClass('active');
    $(this).siblings().removeClass('active');
  });

  function filterClasses(course) {
    if (course === 'all') {
      $('.class-course').addClass('active');
    } else {
      $('.class-course').each(function () {
        const courses = $(this).attr('data-courses') || '';
        if (courses.includes(course)) {
          $(this).addClass('active');
        } else {
          $(this).removeClass('active');
        }
      });
    }
  }

  function filterDuration(duration) {
    if (duration === 'all') {
      $('.class-duration').addClass('active');
    } else {
      $('.class-duration').each(function () {
        const durations = $(this).attr('data-duration') || '';
        if (durations.includes(duration)) {
          $(this).addClass('active');
        } else {
          $(this).removeClass('active');
        }
      });
    }
  }
});


function formatNumber(number) {
  return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function animateNumber(element, targetNumber, duration) {
  const startTime = performance.now();
  const startNumber = 0;

  function updateNumber(currentTime) {
    const elapsedTime = currentTime - startTime;
    const progress = Math.min(elapsedTime / duration, 1);
    const currentNumber = Math.floor(startNumber + progress * (targetNumber - startNumber));

    element.innerText = formatNumber(currentNumber);

    if (progress < 1) {
      requestAnimationFrame(updateNumber);
    }
  }

  requestAnimationFrame(updateNumber);
}

function checkScroll() {
  const numberElements = document.querySelectorAll('.number');
  numberElements.forEach(element => {
    // Periksa jika elemen sudah dianimasikan
    if (!element.classList.contains('animated')) {
      const targetValue = parseInt(element.getAttribute("data-target"), 10);
      const durationValue = parseInt(element.getAttribute("data-duration"), 10);

      // Memeriksa apakah elemen muncul di viewport
      const rect = element.getBoundingClientRect();
      if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
        animateNumber(element, targetValue, durationValue);
        element.classList.add('animated'); // Tandai elemen sudah dianimasikan
      }
    }
  });
}

// Menambah event listener untuk scroll
window.addEventListener('scroll', checkScroll);

$(function () {
  const playerTrack = $("#player-track");
  const bgArtwork = $("#player-bg-artwork");
  const albumName = $("#album-name");
  const trackName = $("#track-name");
  const albumArt = $("#album-art");
  const sArea = $("#seek-bar-container");
  const seekBar = $("#seek-bar");
  const trackTime = $("#track-time");
  const seekTime = $("#seek-time");
  const sHover = $("#s-hover");
  const playPauseButton = $("#play-pause-button");
  const tProgress = $("#current-time");
  const tTime = $("#track-length");
  const playPreviousTrackButton = $("#play-previous");
  const playNextTrackButton = $("#play-next");
  const albums = [
    "Love Accordion & Violin",
    "Warm Inspiring Piano",
    "An Italy"
  ];
  const trackNames = [
    "Song by EddieHoncha",
    "Song by ABCDmusic",
    "Song by original_soundtrack"
  ];
  const albumArtworks = ["_1", "_2", "_3"];
  const trackUrl = [
    "music/Love Accordion & Violin.mp3",
    "music/Warm Inspiring Piano.mp3",
    "music/An Italy.mp3"
  ];

  let bgArtworkUrl,
    i = playPauseButton.find("i"),
    seekT,
    seekLoc,
    seekBarPos,
    cM,
    ctMinutes,
    ctSeconds,
    curMinutes,
    curSeconds,
    durMinutes,
    durSeconds,
    playProgress,
    bTime,
    nTime = 0,
    buffInterval = null,
    tFlag = false,
    currIndex = -1;

  function playPause() {
    setTimeout(function () {
      if (audio.paused) {
        playerTrack.addClass("active");
        albumArt.addClass("active");
        checkBuffering();
        i.attr("class", "fas fa-pause");

        audio.play();
      } else {
        playerTrack.removeClass("active");
        albumArt.removeClass("active");
        clearInterval(buffInterval);
        albumArt.removeClass("buffering");
        i.attr("class", "fas fa-play");
        audio.pause();
      }
    }, 300);
  }

  function showHover(event) {
    seekBarPos = sArea.offset();
    seekT = event.clientX - seekBarPos.left;
    seekLoc = audio.duration * (seekT / sArea.outerWidth());

    sHover.width(seekT);

    cM = seekLoc / 60;

    ctMinutes = Math.floor(cM);
    ctSeconds = Math.floor(seekLoc - ctMinutes * 60);

    if (ctMinutes < 0 || ctSeconds < 0) return;

    if (ctMinutes < 0 || ctSeconds < 0) return;

    if (ctMinutes < 10) ctMinutes = "0" + ctMinutes;
    if (ctSeconds < 10) ctSeconds = "0" + ctSeconds;

    if (isNaN(ctMinutes) || isNaN(ctSeconds)) seekTime.text("--:--");
    else seekTime.text(ctMinutes + ":" + ctSeconds);

    seekTime.css({ left: seekT, "margin-left": "-21px" }).fadeIn(0);
  }

  function hideHover() {
    sHover.width(0);
    seekTime
      .text("00:00")
      .css({ left: "0px", "margin-left": "0px" })
      .fadeOut(0);
  }

  function playFromClickedPos() {
    audio.currentTime = seekLoc;
    seekBar.width(seekT);
    hideHover();
  }

  function updateCurrTime() {
    nTime = new Date();
    nTime = nTime.getTime();

    if (!tFlag) {
      tFlag = true;
      trackTime.addClass("active");
    }

    curMinutes = Math.floor(audio.currentTime / 60);
    curSeconds = Math.floor(audio.currentTime - curMinutes * 60);

    durMinutes = Math.floor(audio.duration / 60);
    durSeconds = Math.floor(audio.duration - durMinutes * 60);

    playProgress = (audio.currentTime / audio.duration) * 100;

    if (curMinutes < 10) curMinutes = "0" + curMinutes;
    if (curSeconds < 10) curSeconds = "0" + curSeconds;

    if (durMinutes < 10) durMinutes = "0" + durMinutes;
    if (durSeconds < 10) durSeconds = "0" + durSeconds;

    if (isNaN(curMinutes) || isNaN(curSeconds)) tProgress.text("00:00");
    else tProgress.text(curMinutes + ":" + curSeconds);

    if (isNaN(durMinutes) || isNaN(durSeconds)) tTime.text("00:00");
    else tTime.text(durMinutes + ":" + durSeconds);

    if (
      isNaN(curMinutes) ||
      isNaN(curSeconds) ||
      isNaN(durMinutes) ||
      isNaN(durSeconds)
    )
      trackTime.removeClass("active");
    else trackTime.addClass("active");

    seekBar.width(playProgress + "%");

    if (playProgress == 100) {
      i.attr("class", "fa fa-play");
      seekBar.width(0);
      tProgress.text("00:00");
      albumArt.removeClass("buffering").removeClass("active");
      clearInterval(buffInterval);
    }
  }

  function checkBuffering() {
    clearInterval(buffInterval);
    buffInterval = setInterval(function () {
      if (nTime == 0 || bTime - nTime > 1000) albumArt.addClass("buffering");
      else albumArt.removeClass("buffering");

      bTime = new Date();
      bTime = bTime.getTime();
    }, 100);
  }

  function selectTrack(flag) {
    if (flag == 0 || flag == 1) ++currIndex;
    else --currIndex;

    if (currIndex > -1 && currIndex < albumArtworks.length) {
      if (flag == 0) i.attr("class", "fa fa-play");
      else {
        albumArt.removeClass("buffering");
        i.attr("class", "fa fa-pause");
      }

      seekBar.width(0);
      trackTime.removeClass("active");
      tProgress.text("00:00");
      tTime.text("00:00");

      currAlbum = albums[currIndex];
      currTrackName = trackNames[currIndex];
      currArtwork = albumArtworks[currIndex];

      audio.src = trackUrl[currIndex];

      nTime = 0;
      bTime = new Date();
      bTime = bTime.getTime();

      if (flag != 0) {
        audio.play();
        playerTrack.addClass("active");
        albumArt.addClass("active");

        clearInterval(buffInterval);
        checkBuffering();
      }

      albumName.text(currAlbum);
      trackName.text(currTrackName);
      albumArt.find("img.active").removeClass("active");
      $("#" + currArtwork).addClass("active");

      bgArtworkUrl = $("#" + currArtwork).attr("src");

      bgArtwork.css({ "background-image": "url(" + bgArtworkUrl + ")" });
    } else {
      if (flag == 0 || flag == 1) --currIndex;
      else ++currIndex;
    }
  }

  function initPlayer() {
    audio = new Audio();

    selectTrack(0);

    audio.loop = false;

    playPauseButton.on("click", playPause);

    sArea.mousemove(function (event) {
      showHover(event);
    });

    sArea.mouseout(hideHover);

    sArea.on("click", playFromClickedPos);

    $(audio).on("timeupdate", updateCurrTime);

    playPreviousTrackButton.on("click", function () {
      selectTrack(-1);
    });
    playNextTrackButton.on("click", function () {
      selectTrack(1);
    });
  }

  initPlayer();
});

$(document).ready(function () {
  $('.hotspot').on('click', function () {
    alert($(this).attr('data-text'));
  });
});





