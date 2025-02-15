

function showOuterModal(itemId) {
    document.getElementById("outerModal" + itemId).style.display = "block";
}

function closeOuterModal(itemId) {
    document.getElementById("outerModal" + itemId).style.display = "none";
}

function showInnerModal1(itemId) {
    document.getElementById("innerModal1" + itemId).style.display = "block";
}

function closeInnerModal1(itemId) {
    document.getElementById("innerModal1" + itemId).style.display = "none";
}

function showInnerModal2(itemId) {
    document.getElementById("innerModal2" + itemId).style.display = "block";
}

function closeInnerModal2(itemId) {
    document.getElementById("innerModal2" + itemId).style.display = "none";
}

document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.copy-btn');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-item-id');
            const textToCopy = document.getElementById("text_" + itemId).innerText;

            copyToClipboard(textToCopy);
        });
    });
});

async function copyToClipboard(text) {
    try {
        await navigator.clipboard.writeText(text);
        alert("Text copied to clipboard!");
    } catch (err) {
        console.error("Error copying text: ", err);
    }
}

function showSection(sectionNumber) {
    var sections = document.getElementsByClassName("section");
    for (var i = 0; i < sections.length; i++) {
      sections[i].style.display = "none";
    }
    document.getElementById("section" + sectionNumber).style.display = "block";
  }
  


  
  function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  }
