package com.redhat;

import dev.langchain4j.service.SystemMessage;
import io.quarkiverse.langchain4j.RegisterAiService;
import io.smallrye.mutiny.Multi;
import jakarta.enterprise.context.SessionScoped;

@SessionScoped
@RegisterAiService
public interface Bot {

    @SystemMessage("""
        You are an AI answering questions.
        Your response must be polite, use the same language as the question, and be relevant to the question.

        When you don't know, respond that you don't know the answer.
        """)
    Multi<String> chat(String userMessage);
}